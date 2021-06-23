%global __brp_check_rpaths %{nil}
%global packname  PubMedMining
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Text-Mining of the 'PubMed' Repository

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-easyPubMed 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-easyPubMed 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
Easy function for text-mining the 'PubMed' repository based on defined
sets of terms. The relationship between fix-terms (related to your
research topic) and pub-terms (terms which pivot around your research
focus) is calculated using the pointwise mutual information algorithm
('PMI'). Church, Kenneth Ward and Hanks, Patrick (1990)
<https://www.aclweb.org/anthology/J90-1003/> A text file is generated with
the 'PMI'-scores for each fix-term. Then for each collocation pairs (a
fix-term + a pub-term), a text file is generated with related article
titles and publishing years. Additional Author section will follow in the
next version updates.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
