%global __brp_check_rpaths %{nil}
%global packname  itdr
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Integral Transformation Methods for SDR in Regression

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-MASS 

%description
The routine, itdr(), which allows to estimate the sufficient dimension
reduction subspaces, i.e., central mean subspace or central subspace in
regression, using Fourier transformation proposed by Zhu and Zeng (2006)
<https:doi.org/10.1198/016214506000000140>, convolution transformation
proposed by Zeng and Zhu (2010) <https:doi.org/10.1016/j.jmva.2009.08.004>
and iterative Hessian transformation methods proposed by Cook and Li
(2002) <https:doi.org/10.1214/aos/1021379861>. The predictor variables can
be consider to have a multivariate normal distribution or an elliptical
contoured distribution. If the distribution of the predictor variables is
unknown, then the predictors' distribution can be estimated by the kernel
density estimation method. Moreover, each of these routines is supported
with a bootstrap procedure to estimate their tuning parameters. That is,
wx() estimates the tuning parameter for the predictor variables, wy()
estimates the tuning parameter for the response variable, and wh()
estimates the bandwidth parameter for the kernel density estimation
method. The function invFM() estimates the central subspace using Fourier
transform approach for inverse dimension reduction method proposed by Weng
and Yin (2018) <https:doi.org/10.1080/10485252.2018.1515432>. The function
d.test() estimates the dimension of the central mean subspace using
hypothesis under invFM(). Moreover, the dsp() function provides the two
distance measures between two subspaces spanned by the columns of two
matrices; Vector correlation proposed by Hooper (1959)
<https:doi.org/10.2307/1909445>, and Trace correlation proposed by
Hotelling (1936) <https:doi.org/10.2307/2333955>.

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
