%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gpci
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Process Capability Indices and Bootstrap Confidence Intervals

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-boot 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-boot 

%description
A comprehensive, generalized framework for computing, estimating, and
validating Generalized Process Capability Indices (GPCIs). Supports
user-supplied probability density functions (PDF/PMF), cumulative
distribution functions (CDF), survival functions (SF), and quantile
functions with uncensored data parameter estimation via Maximum Likelihood
Estimation (MLE). Provides classical and non-normal capability indices,
including Cpy (Maiti, Saha and Nanda, 2010)
<doi:10.1080/16843703.2010.11673233>, Spmk (Dey and Saha, 2019)
<doi:10.1007/s41872-019-00081-4>, CpTk (Saha, Dey and Maiti, 2019)
<doi:10.1007/s13198-019-00789-7>, Cpc (Saha, Dey and Nadarajah, 2022)
<doi:10.1080/02664763.2021.1971632>, CNpmc (Alotaibi, Dey and Saha, 2022)
<doi:10.1155/2022/3135264>, CNpmkc (Saha, Tripathi and Dey, 2024)
<doi:10.1142/S021853932450013X>, CNpk (Saha, Dey and Maiti, 2018)
<doi:10.1080/21681015.2018.1437793>, and Vannman capability indices.
Computes parametric and non-parametric bootstrap confidence intervals at
90%%, 95%%, and 99%% confidence levels using percentile, normal, basic, BCa,
BCp, and studentized bootstrap methods. Evaluates Highest Posterior
Density (HPD) intervals and Heidelberger-Welch convergence diagnostics.
References: Maiti, Saha and Nanda (2010)
<doi:10.1080/16843703.2010.11673233>, Saha, Dey and Maiti (2018)
<doi:10.1080/21681015.2018.1437793>, Dey and Saha (2019)
<doi:10.1007/s41872-019-00081-4>, Saha, Dey and Maiti (2019)
<doi:10.1007/s13198-019-00789-7>, Alotaibi, Dey and Saha (2022)
<doi:10.1155/2022/3135264>, Saha, Dey and Nadarajah (2022)
<doi:10.1080/02664763.2021.1971632>, Saha, Tripathi and Dey (2024)
<doi:10.1142/S021853932450013X>.

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
