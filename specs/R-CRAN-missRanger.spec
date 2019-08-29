%global packname  missRanger
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}
Summary:          Fast Imputation of Missing Values

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FNN >= 1.1
BuildRequires:    R-CRAN-ranger >= 0.10
BuildRequires:    R-stats 
Requires:         R-CRAN-FNN >= 1.1
Requires:         R-CRAN-ranger >= 0.10
Requires:         R-stats 

%description
Alternative implementation of the beautiful 'MissForest' algorithm used to
impute mixed-type data sets by chaining random forests, introduced by
Stekhoven, D.J. and Buehlmann, P. (2012)
<doi:10.1093/bioinformatics/btr597>. Under the hood, it uses the lightning
fast random jungle package 'ranger'. Between the iterative model fitting,
we offer the option of using predictive mean matching. This firstly avoids
imputation with values not already present in the original data (like a
value 0.3334 in 0-1 coded variable). Secondly, predictive mean matching
tries to raise the variance in the resulting conditional distributions to
a realistic level. This would allow e.g. to do multiple imputation when
repeating the call to missRanger(). A formula interface allows to control
which variables should be imputed by which.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
