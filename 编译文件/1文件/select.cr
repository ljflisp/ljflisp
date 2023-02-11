def select_sort(arr)
  arr.each_index do |curr_idx|
    min_idx= (curr_idx...arr.size).#我去,少打1个点你要死啊!
    min_by {|idx| arr[idx]}

    arr[curr_idx],arr[min_idx]= arr[min_idx],arr[curr_idx]
  end
end

def remove_duplicates(arr)
  if arr.size<= 1
   return
  end

  pre_idx= 0
  (1...arr.size).each do |curr_idx|
  if arr[pre_idx]!=arr[curr_idx]
    pre_idx= pre_idx+1
    arr[pre_idx]=arr[curr_idx]
  end
end

arr.delete_at(pre_idx + 1...arr.size)
end

def list_to_set(arr)
  select_sort(arr)
  remove_duplicates(arr)
end


list_of_lists = [
  [] of Int32,
   [1],
   [1,1],
   [1,2],
   [1,1,2],
   [1,2,2],
   [1,1,2,2],
   [1,2,3,4],
   [1,2,3,3,4],
   [1,2,3,4,4],
   [1,3,2,4,3,2,1,2,1],
   [4,5,6,7,8,1,2,3,9],
   [1,4,3]
]
list_of_lists.each do |list|
print "list_of_lists(#{list}) = "
list_to_set(list)
puts "#{list}"
end