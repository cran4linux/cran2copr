%global __brp_check_rpaths %{nil}
%global packname  DataCombine
%global packver   0.2.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.21
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for Easily Combining and Cleaning Data Sets

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.4
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-dplyr >= 0.4
Requires:         R-CRAN-data.table 

%description
Tools for combining and cleaning data sets, particularly with grouped and
time series data.

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
%{rlibdir}/%{packname}
