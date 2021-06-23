%global __brp_check_rpaths %{nil}
%global packname  ILS
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Interlaboratory Study

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-depthTools 
BuildRequires:    R-CRAN-fda.usc 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
Requires:         R-lattice 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-depthTools 
Requires:         R-CRAN-fda.usc 
Requires:         R-MASS 
Requires:         R-stats 

%description
It performs interlaboratory studies (ILS) to detect those laboratories
that provide non-consistent results when comparing to others. It permits
to work simultaneously with various testing materials, from standard
univariate, and functional data analysis (FDA) perspectives. The
univariate approach based on ASTM E691-08 consist of estimating the
Mandel's h and k statistics to identify those laboratories that provide
more significant different results, testing also the presence of outliers
by Cochran and Grubbs tests, Analysis of variance (ANOVA) techniques are
provided (F and Tuckey tests) to test differences in means corresponding
to different laboratories per each material. Taking into account the
functional nature of data retrieved in analytical chemistry, applied
physics and engineering (spectra, thermograms, etc.). ILS package provides
a FDA approach for finding the Mandel's k and h statistics distribution by
smoothing bootstrap resampling.

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
%doc %{rlibdir}/%{packname}/CHANGES
%{rlibdir}/%{packname}/INDEX
