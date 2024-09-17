%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SVMD
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spearman Variational Mode Decomposition

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-VMDecomp 
BuildRequires:    R-stats 
Requires:         R-CRAN-VMDecomp 
Requires:         R-stats 

%description
In practice, it is difficult to determine the number of decomposition
modes, K, for Variational Mode Decomposition (VMD). To overcome this
issue, this study offers Spearman Variational Mode Decomposition (SVMD), a
method that uses the Spearman correlation coefficient to calculate the
ideal mode number. Unlike the Pearson correlation coefficient, which only
returns a perfect value when X and Y are linearly connected, the Spearman
correlation can be calculated without knowing the probability
distributions of X and Y. The Spearman correlation coefficient, also
called Spearman's rank correlation coefficient, is a subset of a wider
correlation coefficient. As VMD decomposes a signal, the Spearman
correlation coefficient between the reconstructed and original sequences
rises as the mode number K increases. Once the signal has been fully
decomposed, subsequent increases in K cause the correlation to gradually
level off. When the correlation reaches a specific level, VMD is said to
have adequately decomposed the signal. Numerous experiments revealed that
a threshold of 0.997 produces the best denoising effect, so the threshold
is set at 0.997. This package has been developed using concept of Yang et
al. (2021)<doi:10.1016/j.aej.2021.01.055>.

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
