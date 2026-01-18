%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RFAE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Autoencoding Random Forests

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-RSpectra 
Requires:         R-stats 
Requires:         R-CRAN-tibble 

%description
Autoencoding Random Forests ('RFAE') provide a method to autoencode
mixed-type tabular data using Random Forests ('RF'), which involves
projecting the data to a latent feature space of user-chosen
dimensionality (usually a lower dimension), and then decoding the latent
representations back into the input space. The encoding stage is useful
for feature engineering and data visualisation tasks, akin to how
principal component analysis ('PCA') is used, and the decoding stage is
useful for compression and denoising tasks. At its core, 'RFAE' is a
post-processing pipeline on a trained random forest model. This means that
it can accept any trained RF of 'ranger' object type: 'RF', 'URF' or
'ARF'. Because of this, it inherits Random Forests' robust performance and
capacity to seamlessly handle mixed-type tabular data. For more details,
see Vu et al. (2025) <doi:10.48550/arXiv.2505.21441>.

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
