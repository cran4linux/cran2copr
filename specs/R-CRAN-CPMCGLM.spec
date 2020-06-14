%global packname  CPMCGLM
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          2%{?dist}
Summary:          Correction of the P-Value after Multiple Coding in GeneralizedLinear Models

License:          GPL (> 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-abind 

%description
We propose to determine the correction of the significance level after
multiple coding of an explanatory variable in Generalized Linear Model.
The different methods of correction of the p-value are the Single step
Bonferroni procedure, and resampling based methods developed by
P.H.Westfall in 1993. Resampling methods are based on the permutation and
the parametric bootstrap procedure. If some continuous, and dichotomous
transformations are performed this package offers an exact correction of
the p-value developed by B.Liquet & D.Commenges in 2005. The naive method
with no correction is also available.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
