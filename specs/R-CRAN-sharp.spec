%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sharp
%global packver   1.4.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.7
Release:          1%{?dist}%{?buildtag}
Summary:          Stability-enHanced Approaches using Resampling Procedures

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-withr >= 2.4.0
BuildRequires:    R-CRAN-fake >= 1.4.0
BuildRequires:    R-CRAN-glassoFast >= 1.0.0
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-beepr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-withr >= 2.4.0
Requires:         R-CRAN-fake >= 1.4.0
Requires:         R-CRAN-glassoFast >= 1.0.0
Requires:         R-CRAN-abind 
Requires:         R-CRAN-beepr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-glmnet 
Requires:         R-grDevices 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-Rdpack 

%description
In stability selection (N Meinshausen, P Bühlmann (2010)
<doi:10.1111/j.1467-9868.2010.00740.x>) and consensus clustering (S Monti
et al (2003) <doi:10.1023/A:1023949509487>), resampling techniques are
used to enhance the reliability of the results. In this package (B
Bodinier et al (2025) <doi:10.18637/jss.v112.i05>), hyper-parameters are
calibrated by maximising model stability, which is measured under the null
hypothesis that all selection (or co-membership) probabilities are
identical (B Bodinier et al (2023a) <doi:10.1093/jrsssc/qlad058> and B
Bodinier et al (2023b) <doi:10.1093/bioinformatics/btad635>). Functions
are readily implemented for the use of LASSO regression, sparse PCA,
sparse (group) PLS or graphical LASSO in stability selection, and
hierarchical clustering, partitioning around medoids, K means or Gaussian
mixture models in consensus clustering.

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
