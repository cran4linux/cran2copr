%global packname  MixedPsy
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}%{?buildtag}
Summary:          Statistical Tools for the Analysis of Psychophysical Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-beepr 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-brglm 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-mnormt 
Requires:         R-CRAN-beepr 
Requires:         R-boot 
Requires:         R-CRAN-brglm 
Requires:         R-CRAN-lme4 
Requires:         R-Matrix 
Requires:         R-CRAN-mnormt 

%description
Tools for the analysis of psychophysical data. This package allows to
estimate the Point of Subjective Equivalence (PSE) and the Just Noticeable
Difference (JND), either from a psychometric function or from a
Generalized Linear Mixed Model (GLMM). Additionally, the package allows
plotting the fitted models and the response data, simulating psychometric
functions of different shapes, and simulating data sets. For a description
of the use of GLMMs applied to psychophysical data, refer to Moscatelli et
al. (2012), <doi:10.1167/12.11.26>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
