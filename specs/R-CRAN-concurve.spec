%global packname  concurve
%global packver   2.7.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7.7
Release:          1%{?dist}%{?buildtag}
Summary:          Computes & Plots Compatibility (Confidence), Surprisal, & Likelihood Distributions

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-bcaboot 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbmcapply 
BuildRequires:    R-CRAN-ProfileLikelihood 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-methods 
Requires:         R-CRAN-bcaboot 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-officer 
Requires:         R-parallel 
Requires:         R-CRAN-pbmcapply 
Requires:         R-CRAN-ProfileLikelihood 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-survminer 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Computes compatibility (confidence) distributions along with their
corresponding P-values, S-values, and likelihoods. The intervals can be
plotted to form the distributions themselves. Functions can be compared to
one another to see how much they overlap. Results can be exported to
Microsoft Word, Powerpoint, and TeX documents. The package currently
supports resampling methods, computing differences, generalized linear
models, mixed-effects models, survival analysis, and meta-analysis. These
methods are discussed by Schweder T, Hjort NL. (2016, ISBN:9781316445051)
and Rafi Z, Greenland S. (2020) <doi:10.1186/s12874-020-01105-9>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
