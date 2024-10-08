%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GRAPE
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Gene-Ranking Analysis of Pathway Expression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Gene-Ranking Analysis of Pathway Expression (GRAPE) is a tool for
summarizing the consensus behavior of biological pathways in the form of a
template, and for quantifying the extent to which individual samples
deviate from the template. GRAPE templates are based only on the relative
rankings of the genes within the pathway and can be used for
classification of tissue types or disease subtypes. GRAPE can be used to
represent gene-expression samples as vectors of pathway scores, where each
pathway score indicates the departure from a given collection of reference
samples. The resulting pathway- space representation can be used as the
feature set for various applications, including survival analysis and
drug-response prediction. Users of GRAPE should use the following
citation: Klein MI, Stern DF, and Zhao H. GRAPE: A pathway template method
to characterize tissue-specific functionality from gene expression
profiles. BMC Bioinformatics, 18:317 (June 2017).

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
