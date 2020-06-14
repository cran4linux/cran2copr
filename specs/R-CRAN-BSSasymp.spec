%global packname  BSSasymp
%global packver   1.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          2%{?dist}
Summary:          Asymptotic Covariance Matrices of Some BSS Mixing and UnmixingMatrix Estimates

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-fICA >= 1.0.2
BuildRequires:    R-CRAN-JADE 
Requires:         R-CRAN-fICA >= 1.0.2
Requires:         R-CRAN-JADE 

%description
Functions to compute the asymptotic covariance matrices of mixing and
unmixing matrix estimates of the following blind source separation (BSS)
methods: symmetric and squared symmetric FastICA, regular and adaptive
deflation-based FastICA, FOBI, JADE, AMUSE and deflation-based and
symmetric SOBI. Also functions to estimate these covariances based on data
are available. For details, see Miettinen et al. (2015)
<doi:10.1214/15-STS520>, Miettinen et al. (2016) <doi:10.1111/jtsa.12159>,
Miettinen et al. (2017) <doi:10.1016/j.sigpro.2016.08.028>, Miettinen et
al. (2017) <doi:10.18637/jss.v076.i02>, and references therein.

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
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
