%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ashapesampler
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generating Alpha Shapes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-alphahull 
BuildRequires:    R-CRAN-alphashape3d 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rvcg 
BuildRequires:    R-CRAN-TDA 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-alphahull 
Requires:         R-CRAN-alphashape3d 
Requires:         R-CRAN-truncnorm 
Requires:         R-stats 
Requires:         R-CRAN-Rvcg 
Requires:         R-CRAN-TDA 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-dplyr 

%description
Understanding morphological variation is an important task in many
applications. Recent studies in computational biology have focused on
developing computational tools for the task of sub-image selection which
aims at identifying structural features that best describe the variation
between classes of shapes. A major part in assessing the utility of these
approaches is to demonstrate their performance on both simulated and real
datasets. However, when creating a model for shape statistics, real data
can be difficult to access and the sample sizes for these data are often
small due to them being expensive to collect. Meanwhile, the landscape of
current shape simulation methods has been mostly limited to approaches
that use black-box inference---making it difficult to systematically
assess the power and calibration of sub-image models. In this R package,
we introduce the alpha-shape sampler: a probabilistic framework for
simulating realistic 2D and 3D shapes based on probability distributions
which can be learned from real data or explicitly stated by the user. The
'ashapesampler' package supports two mechanisms for sampling shapes in two
and three dimensions. The first, empirically sampling based on an existing
data set, was highlighted in the original main text of the paper. The
second, probabilistic sampling from a known distribution, is the
computational implementation of the theory derived in that paper. Work
based on Winn-Nunez et al. (2024) <doi:10.1101/2024.01.09.574919>.

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
