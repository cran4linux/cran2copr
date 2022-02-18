%global __brp_check_rpaths %{nil}
%global packname  hacksig
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Tidy Framework to Hack Gene Expression Signatures

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.0.5
BuildRequires:    R-CRAN-tibble >= 3.1.5
BuildRequires:    R-CRAN-future.apply >= 1.8.1
BuildRequires:    R-CRAN-tidyr >= 1.1.4
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-rlang >= 0.4.11
Requires:         R-stats >= 4.0.5
Requires:         R-CRAN-tibble >= 3.1.5
Requires:         R-CRAN-future.apply >= 1.8.1
Requires:         R-CRAN-tidyr >= 1.1.4
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-rlang >= 0.4.11

%description
A collection of cancer transcriptomics gene signatures as well as a simple
and tidy interface to compute single sample enrichment scores either with
the original procedure or with three alternatives: the "combined z-score"
of Lee et al. (2008) <doi:10.1371/journal.pcbi.1000217>, the "single
sample GSEA" of Barbie et al. (2009) <doi:10.1038/nature08460> and the
"singscore" of Foroutan et al. (2018) <doi:10.1186/s12859-018-2435-4>. The
'get_sig_info()' function can be used to retrieve information about each
signature implemented.

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
