%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MAP
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multimodal Automated Phenotyping

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-flexmix >= 2.3.14
BuildRequires:    R-CRAN-Matrix >= 1.2.10
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-flexmix >= 2.3.14
Requires:         R-CRAN-Matrix >= 1.2.10
Requires:         R-CRAN-magrittr 

%description
Electronic health records (EHR) linked with biorepositories are a powerful
platform for translational studies. A major bottleneck exists in the
ability to phenotype patients accurately and efficiently. Towards that
end, we developed an automated high-throughput phenotyping method
integrating International Classification of Diseases (ICD) codes and
narrative data extracted using natural language processing (NLP).
Specifically, our proposed method, called MAP (Map Automated Phenotyping
algorithm), fits an ensemble of latent mixture models on aggregated ICD
and NLP counts along with healthcare utilization. The MAP algorithm yields
a predicted probability of phenotype for each patient and a threshold for
classifying subjects with phenotype yes/no (See Katherine P. Liao, et al.
(2019) <doi:10.1093/jamia/ocz066>.).

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
