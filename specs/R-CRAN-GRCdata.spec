%global __brp_check_rpaths %{nil}
%global packname  GRCdata
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Parameter Inference and Optimal Designs for Grouped and/orRight-Censored Count Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-cubature 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-cubature 

%description
We implement two main functions. The first function uses a given grouped
and/or right-censored grouping scheme and empirical data to infer
parameters, and implements chi-square goodness-of-fit tests. The second
function searches for the global optimal grouping scheme of grouped and/or
right-censored count responses in surveys.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
