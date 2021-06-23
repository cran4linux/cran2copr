%global __brp_check_rpaths %{nil}
%global packname  MCMC.OTU
%global packver   1.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.10
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Analysis of Multivariate Counts Data in DNA Metabarcoding and Ecology

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCglmm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-MCMCglmm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-coda 

%description
Poisson-lognormal generalized linear mixed model analysis of multivariate
counts data using MCMC, aiming to infer the changes in relative
proportions of individual variables. The package was originally designed
for sequence-based analysis of microbial communities ("metabarcoding",
variables = operational taxonomic units, OTUs), but can be used for other
types of multivariate counts, such as in ecological applications
(variables = species). The results are summarized and plotted using
'ggplot2' functions. Includes functions to remove sample and variable
outliers and reformat counts into normalized log-transformed values for
correlation and principal component/coordinate analysis. Walkthrough and
examples:
http://www.bio.utexas.edu/research/matz_lab/matzlab/Methods_files/walkthroughExample_mcmcOTU_R.txt.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
