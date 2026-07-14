%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  openNLP
%global packver   0.2-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Apache OpenNLP Tools Interface

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-openNLPdata >= 1.5.3.1
BuildRequires:    R-CRAN-rJava >= 0.6.3
BuildRequires:    R-CRAN-NLP >= 0.1.6.3
Requires:         R-CRAN-openNLPdata >= 1.5.3.1
Requires:         R-CRAN-rJava >= 0.6.3
Requires:         R-CRAN-NLP >= 0.1.6.3

%description
An interface to the Apache OpenNLP tools (version 1.5.3). The Apache
OpenNLP library is a machine learning based toolkit for the processing of
natural language text written in Java. It supports the most common NLP
tasks, such as tokenization, sentence segmentation, part-of-speech
tagging, named entity extraction, chunking, parsing, and coreference
resolution. See <https://opennlp.apache.org/> for more information.

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
