%global __brp_check_rpaths %{nil}
%global packname  textrank
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Summarize Text by Ranking Sentences and Finding Keywords

License:          MPL-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-utils 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-digest 

%description
The 'textrank' algorithm is an extension of the 'Pagerank' algorithm for
text. The algorithm allows to summarize text by calculating how sentences
are related to one another. This is done by looking at overlapping
terminology used in sentences in order to set up links between sentences.
The resulting sentence network is next plugged into the 'Pagerank'
algorithm which identifies the most important sentences in your text and
ranks them. In a similar way 'textrank' can also be used to extract
keywords. A word network is constructed by looking if words are following
one another. On top of that network the 'Pagerank' algorithm is applied to
extract relevant words after which relevant words which are following one
another are combined to get keywords. More information can be found in the
paper from Mihalcea, Rada & Tarau, Paul (2004)
<https://www.aclweb.org/anthology/W04-3252/>.

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
