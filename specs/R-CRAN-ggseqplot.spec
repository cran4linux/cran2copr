%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggseqplot
%global packver   0.8.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.7
Release:          1%{?dist}%{?buildtag}
Summary:          Render Sequence Plots using 'ggplot2'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-TraMineR >= 2.2.5
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-forcats >= 1.0.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-ggh4x 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-usethis 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-TraMineR >= 2.2.5
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-forcats >= 1.0.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-ggh4x 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-usethis 

%description
A set of wrapper functions that mainly re-produces most of the sequence
plots rendered with TraMineR::seqplot(). Whereas 'TraMineR' uses base R to
produce the plots this library draws on 'ggplot2'. The plots are produced
on the basis of a sequence object defined with TraMineR::seqdef(). The
package automates the reshaping and plotting of sequence data. Resulting
plots are of class 'ggplot', i.e. components can be added and tweaked
using '+' and regular 'ggplot2' functions.

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
