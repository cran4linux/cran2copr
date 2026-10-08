%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aersn
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Affine-Equivariant Adjusted-Range Self-Normalization for Time-Series Inference

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sandwich >= 3.0.0
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-sandwich >= 3.0.0
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-lpSolve 
Requires:         R-stats 
Requires:         R-utils 

%description
Tuning-free inference on fixed-dimensional parameters of dependent time
series using affine-equivariant adjusted-range self-normalization. The
centered partial-sum path of estimated influence contributions is
normalized by its increment hull, the convex hull of all path increments.
The gauge of the hull provides an asymptotically pivotal test statistic
and an affine-equivariant confidence region without estimating the
long-run covariance matrix, and its support function gives simultaneous
confidence intervals for linear contrasts. For a single parameter the
construction reduces exactly to adjusted-range self-normalization, whose
limiting distribution is available in closed form. The Brownian reference
law is simulated on a grid matched to the sample size or a supplied common
variance-accumulation profile; inference for dependent observations
remains asymptotic. Five further methods are provided for comparison on
the same estimate and influence contributions: componentwise adjusted
ranges after lag-zero partial prewhitening, quadratic self-normalization
following Shao (2010) <doi:10.1111/j.1467-9868.2009.00737.x>, kernel
long-run covariance estimation with automatic bandwidth selection
following Andrews (1991) <doi:10.2307/2938229> and Newey and West (1994)
<doi:10.2307/2297912>, Bartlett fixed-b inference following Kiefer and
Vogelsang (2005) <doi:10.1017/S0266466605050565>, and the equal-weighted
cosine method of Lazarus, Lewis, Stock and Watson (2018)
<doi:10.1080/07350015.2018.1506926>. Model interfaces are provided for
sample means, linear regression, smooth generalized method of moments, and
conditional likelihood scores; other estimators are handled through
user-supplied influence contributions. The methods follow Hong, Lin,
Linton, Newey and Sun (2026), Cambridge Working Papers in Economics No.
2678
<https://www.janeway.econ.cam.ac.uk/publication/affine-equivariant-adjusted-range-self-normalization>
and, for the scalar case, Hong, Linton, McCabe, Sun and Wang (2024)
<doi:10.1016/j.jeconom.2023.105603>.

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
