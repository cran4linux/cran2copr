%global __brp_check_rpaths %{nil}
%global packname  W2CWM2C
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Graphical Tool for Wavelet (Cross) Correlation and Wavelet Multiple (Cross) Correlation Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.1
Requires:         R-core >= 2.14.1
BuildArch:        noarch
BuildRequires:    R-CRAN-waveslim 
BuildRequires:    R-CRAN-wavemulcor 
BuildRequires:    R-CRAN-colorspace 
Requires:         R-CRAN-waveslim 
Requires:         R-CRAN-wavemulcor 
Requires:         R-CRAN-colorspace 

%description
Set of functions that improves the graphical presentations of the
functions: wave.correlation and spin.correlation (waveslim package,
Whitcher 2012) and the wave.multiple.correlation and
wave.multiple.cross.correlation (wavemulcor package, Fernandez-Macho
2012b). The plot outputs (heatmaps) can be displayed in the screen or can
be saved as PNG or JPG images or as PDF or EPS formats. The W2CWM2C
package also helps to handle the (input data) multivariate time series
easily as a list of N elements (times series) and provides a multivariate
data set (dataexample) to exemplify its use. A description of the package
was published in a scientific paper: Polanco-Martinez and Fernandez-Macho
(2014), <doi:10.1109/MCSE.2014.96>.

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
