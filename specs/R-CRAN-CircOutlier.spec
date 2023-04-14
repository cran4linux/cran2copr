%global __brp_check_rpaths %{nil}
%global packname  CircOutlier
%global packver   3.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.3
Release:          3%{?dist}%{?buildtag}
Summary:          Detection of Outliers in Circular-Circular Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-CircStats 
BuildRequires:    R-CRAN-circular 
Requires:         R-CRAN-CircStats 
Requires:         R-CRAN-circular 

%description
Detection of outliers in circular-circular regression models, modifying
its and estimating of models parameters.

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
