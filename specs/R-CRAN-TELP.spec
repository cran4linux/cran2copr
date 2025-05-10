%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TELP
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Social Representation Theory Application: The Free Evocation of Words Technique

License:          GPL (> 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-arulesViz 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-wordcloud 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-arules 
Requires:         R-CRAN-arulesViz 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 

%description
Using The Free Evocation of Words Technique method with some functions,
this package will make a social representation and other analysis. The
Free Evocation of Words Technique consists of collecting a number of words
evoked by a subject facing exposure to an inducer term. The purpose of
this technique is to understand the relationships created between words
evoked by the individual and the inducer term. This technique is included
in the theory of social representations, therefore, on the information
transmitted by an individual, seeks to create a profile that define a
social group.

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
