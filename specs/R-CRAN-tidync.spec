%global packname  tidync
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          3%{?dist}
Summary:          A Tidy Approach to 'NetCDF' Data Exploration and Extraction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RNetCDF >= 1.9.1
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-ncmeta >= 0.2.0
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-RNetCDF >= 1.9.1
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-ncmeta >= 0.2.0
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Tidy tools for 'NetCDF' data sources. Explore the contents of a 'NetCDF'
source (file or URL) presented as variables organized by grid with a
database-like interface. The hyper_filter() interactive function
translates the filter value or index expressions to array-slicing form. No
data is read until explicitly requested, as a data frame or list of arrays
via hyper_tibble() or hyper_array().

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/blog-01
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/erddap
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
