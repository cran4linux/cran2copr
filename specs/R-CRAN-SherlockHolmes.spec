%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SherlockHolmes
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Building a Concordance of Terms in a Series of Texts

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-qpdf 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dpseg 
BuildRequires:    R-CRAN-tableHTML 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-stargazer 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-textBoxPlacement 
BuildRequires:    R-CRAN-plot.matrix 
BuildRequires:    R-CRAN-devtools 
Requires:         R-CRAN-qpdf 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dpseg 
Requires:         R-CRAN-tableHTML 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-stargazer 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-textBoxPlacement 
Requires:         R-CRAN-plot.matrix 
Requires:         R-CRAN-devtools 

%description
Compute the frequency distribution of a search term in a series of texts.
For example, Arthur Conan Doyle wrote a total of 60 Sherlock Holmes
stories, comprised of 54 short stories and 4 longer novels. I wanted to
test my own subjective impression that, in many of the stories, Sherlock
Holmes' popularity was used as bait to induce the reader to read a story
that is essentially not primarily a Sherlock Holmes story. I used the term
"Holmes" as a search pattern, since Watson would frequently address him by
name, or use his name to describe something that he was doing. My
hypothesis is that the frequency distribution of the search pattern
"Holmes" is a good proxy for the degree to which a story is or is not
truly a Sherlock Holmes story. The results are presented in a manuscript
that is available as a vignette and online at
<https://barryzee.github.io/Concordance/index.html>.

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
