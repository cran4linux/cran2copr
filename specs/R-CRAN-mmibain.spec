%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mmibain
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Informative Hypotheses Evaluation Web Applications

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bain 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-mmcards 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
Requires:         R-CRAN-bain 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-car 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-mmcards 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 

%description
Researchers often have expectations about the relations between means of
different groups or standardized regression coefficients; using
informative hypothesis testing to incorporate these expectations into the
analysis through order constraints increases statistical power Vanbrabant
and Rosseel (2020) <doi:10.4324/9780429273872-14>. Another valuable tool,
the Bayes factor, can evaluate evidence for multiple hypotheses without
concerns about multiple testing, and can be used in Bayesian updating
Hoijtink, Mulder, van Lissa & Gu (2019) <doi:10.1037/met0000201>. The
'bain' R package enables informative hypothesis testing using the Bayes
factor. The 'mmibain' package provides 'shiny' web applications based on
'bain'. The RepliCrisis() function launches a 'shiny' card game to
simulate the evaluation of replication studies while the mmibain()
function launches a 'shiny' application to fit Bayesian informative
hypotheses evaluation models from 'bain'.

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
