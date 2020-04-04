%global packname  survey
%global packver   4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0
Release:          1%{?dist}
Summary:          Analysis of Complex Survey Samples

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mitools >= 2.4
BuildRequires:    R-grid 
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
BuildRequires:    R-survival 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-splines 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-mitools >= 2.4
Requires:         R-grid 
Requires:         R-methods 
Requires:         R-Matrix 
Requires:         R-survival 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-splines 
Requires:         R-lattice 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-numDeriv 

%description
Summary statistics, two-sample tests, rank tests, generalised linear
models, cumulative link models, Cox models, loglinear models, and general
maximum pseudolikelihood estimation for multistage stratified,
cluster-sampled, unequally weighted survey samples. Variances by Taylor
series linearisation or replicate weights. Post-stratification,
calibration, and raking. Two-phase subsampling designs. Graphics. PPS
sampling without replacement. Principal components, factor analysis.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/api.db
%doc %{rlibdir}/%{packname}/BUGS
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYING
%doc %{rlibdir}/%{packname}/disclaimer
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/porting.to.S
%doc %{rlibdir}/%{packname}/twostage.pdf
%doc %{rlibdir}/%{packname}/ucla-examples.pdf
%{rlibdir}/%{packname}/INDEX
