%global packname  RobRex
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Optimally Robust Influence Curves for Regression and Scale

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-distr >= 2.8.0
BuildRequires:    R-CRAN-ROptRegTS >= 1.2.0
BuildRequires:    R-CRAN-RandVar >= 1.2.0
BuildRequires:    R-CRAN-RobAStBase >= 1.2.0
BuildRequires:    R-methods 
Requires:         R-CRAN-distr >= 2.8.0
Requires:         R-CRAN-ROptRegTS >= 1.2.0
Requires:         R-CRAN-RandVar >= 1.2.0
Requires:         R-CRAN-RobAStBase >= 1.2.0
Requires:         R-methods 

%description
Functions for the determination of optimally robust influence curves in
case of linear regression with unknown scale and standard normal
distributed errors where the regressor is random.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/scripts
%doc %{rlibdir}/%{packname}/TOBEDONE
%{rlibdir}/%{packname}/INDEX
