%global packname  stringb
%global packver   0.1.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.13
Release:          1%{?dist}
Summary:          Convenient Base R String Handling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-backports 
Requires:         R-graphics 
Requires:         R-tools 
Requires:         R-CRAN-backports 

%description
Base R already ships with string handling capabilities 'out- of-the-box'
but lacks streamlined function names and workflow. The 'stringi'
('stringr') package on the other hand has well named functions, extensive
Unicode support and allows for a streamlined workflow. On the other hand
it adds dependencies and regular expression interpretation between base R
functions and 'stringi' functions might differ. This packages aims at
providing a solution to the use case of unwanted dependencies on the one
hand but the need for streamlined text processing on the other. The
packages' functions are solely based on wrapping base R functions into
'stringr'/'stringi' like function names. Along the way it adds one or two
extra functions and last but not least provides all functions as generics,
therefore allowing for adding methods for other text structures besides
plain character vectors.

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
%doc %{rlibdir}/%{packname}/testfiles
%{rlibdir}/%{packname}/INDEX
