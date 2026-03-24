%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MultiResponseR
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Data from Multiple-Response Questionnaires

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ellipse 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides a multiple-response chi-square framework for the analysis of
contingency tables arising from multiple-response questionnaires, such as
check-all-that-apply tasks, where response options are crossed with a
known grouping factor. The framework accommodates within-block (e.g.,
within-subject) designs, as commonly encountered in sensory evaluation. It
comprises a multiple-response chi-square test of homogeneity with an
associated dimensionality test, a multiple-response Correspondence
Analysis (CA), and per-cell multiple-response hypergeometric tests. These
methods extend their classical counterparts by grounding inference in a
null model that properly accounts for the multiple-response nature of the
data, treating evaluations, rather than individual citations, as the
experimental units, yielding more statistically valid conclusions than
standard contingency table analyses. Details may be found in Mahieu,
Schlich, Visalli, and Cardot (2021). <doi:10.1016/j.foodqual.2021.104256>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
