%global packname  nparMD
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Nonparametric Analysis of Multivariate Data in Factorial Designs

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-matrixcalc 
Requires:         R-MASS 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-Formula 
Requires:         R-methods 
Requires:         R-stats 

%description
Analysis of multivariate data with two-way completely randomized factorial
design. The analysis is based on fully nonparametric, rank-based methods
and uses test statistics based on the Dempster's ANOVA, Wilk's Lambda,
Lawley-Hotelling and Bartlett-Nanda-Pillai criteria. The multivariate
response is allowed to be ordinal, quantitative, binary or a mixture of
the different variable types. The package offers two functions performing
the analysis, one for small and the other for large sample sizes. The
underlying methodology is largely described in Bathke and Harrar (2016)
<doi:10.1007/978-3-319-39065-9_7> and in Munzel and Brunner (2000)
<doi:10.1016/S0378-3758(99)00212-8>.

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
