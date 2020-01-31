%global packname  usefun
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}
Summary:          A Collection of Useful Functions by John

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
A set of general functions that I have used in various projects and in
other R packages. They support some miscellaneous operations on data
frames, matrices and vectors: adding a row on a ternary (3-value)
data.frame based on positive and negative vector-indicators, rearranging a
list of data.frames by rownames, pruning rows or columns of a data.frame
that contain only one specific value given by the user, checking for
matrix equality, pruning and reordering a vector according to the common
elements between its names and elements of another given vector, finding
the non-common elements between two vectors (outer-section), normalization
of a vector, matrix or data.frame's numeric values in a specified range,
pretty printing of vector names and values in an R notebook (common names
and values between two vectors also supported), retrieving the parent
directory of any string path, checking whether a numeric value is inside a
given interval, trim the decimal points of a given numeric value, quick
saving of data to a file, making a multiple densities plot and a color bar
plot and executing a plot string expression while generating the result to
the specified file format.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
