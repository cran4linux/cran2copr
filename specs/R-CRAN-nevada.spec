%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nevada
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Network-Valued Data Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-flipr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-tsne 
BuildRequires:    R-CRAN-umap 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-rgeomstats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-flipr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-tsne 
Requires:         R-CRAN-umap 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-rgeomstats 

%description
A flexible statistical framework for network-valued data analysis. It
leverages the complexity of the space of distributions on graphs by using
the permutation framework for inference as implemented in the 'flipr'
package. Currently, only the two-sample testing problem is covered and
generalization to k samples and regression will be added in the future as
well. It is a 4-step procedure where the user chooses a suitable
representation of the networks, a suitable metric to embed the
representation into a metric space, one or more test statistics to target
specific aspects of the distributions to be compared and a formula to
compute the permutation p-value. Two types of inference are provided: a
global test answering whether there is a difference between the
distributions that generated the two samples and a local test for
localizing differences on the network structure. The latter is assumed to
be shared by all networks of both samples. References: Lovato, I., Pini,
A., Stamm, A., Vantini, S. (2020) "Model-free two-sample test for
network-valued data" <doi:10.1016/j.csda.2019.106896>; Lovato, I., Pini,
A., Stamm, A., Taquet, M., Vantini, S. (2021) "Multiscale null hypothesis
testing for network-valued data: Analysis of brain networks of patients
with autism" <doi:10.1111/rssc.12463>.

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
