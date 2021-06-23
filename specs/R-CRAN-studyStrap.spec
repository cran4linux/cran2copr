%global __brp_check_rpaths %{nil}
%global packname  studyStrap
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Study Strap and Multi-Study Learning Algorithms

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-pls >= 2.7.1
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-nnls >= 1.4
BuildRequires:    R-CRAN-tidyverse >= 1.2.1
BuildRequires:    R-CRAN-CCA >= 1.2
BuildRequires:    R-CRAN-MatrixCorrelation >= 0.9.2
BuildRequires:    R-CRAN-dplyr >= 0.8.2
BuildRequires:    R-CRAN-caret 
Requires:         R-CRAN-pls >= 2.7.1
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-nnls >= 1.4
Requires:         R-CRAN-tidyverse >= 1.2.1
Requires:         R-CRAN-CCA >= 1.2
Requires:         R-CRAN-MatrixCorrelation >= 0.9.2
Requires:         R-CRAN-dplyr >= 0.8.2
Requires:         R-CRAN-caret 

%description
Implements multi-study learning algorithms such as merging, the
study-specific ensemble (trained-on-observed-studies ensemble) the study
strap, the covariate-matched study strap, covariate-profile similarity
weighting, and stacking weights. Embedded within the 'caret' framework,
this package allows for a wide range of single-study learners (e.g.,
neural networks, lasso, random forests). The package offers over 20
default similarity measures and allows for specification of custom
similarity measures for covariate-profile similarity weighting and an
accept/reject step. This implements methods described in Loewinger,
Kishida, Patil, and Parmigiani. (2019) <doi:10.1101/856385>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
