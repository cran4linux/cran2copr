%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  INFOSET
%global packver   4.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Computing a New Informative Distribution Set of Asset Returns

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-mixtools 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-mixtools 
Requires:         R-stats 
Requires:         R-graphics 

%description
Estimation of the most-left informative set of gross returns (i.e., the
informative set). The procedure to compute the informative set adjusts the
method proposed by Mariani et al. (2022a) <doi:10.1007/s11205-020-02440-6>
and Mariani et al. (2022b) <doi:10.1007/s10287-022-00422-2> to gross
returns of financial assets. This is accomplished through an adaptive
algorithm that identifies sub-groups of gross returns in each iteration by
approximating their distribution with a sequence of two-component
log-normal mixtures. These sub-groups emerge when a significant change in
the distribution occurs below the median of the financial returns, with
their boundary termed as the “change point" of the mixture. The process
concludes when no further change points are detected. The outcome
encompasses parameters of the leftmost mixture distributions and change
points of the analyzed financial time series. The functionalities of the
INFOSET package include: (i) modelling asset distribution detecting the
parameters which describe left tail behaviour (infoset function), (ii)
clustering, (iii) labeling of the financial series for predictive and
classification purposes through a Left Risk measure based on the first
change point (LR_cp function) (iv) portfolio construction
(ptf_construction function). The package also provide a specific function
to construct rolling windows of different length size and overlapping
time.

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
