%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sbert
%global packver   0.5.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.8
Release:          1%{?dist}%{?buildtag}
Summary:          Topic Modeling with 'Sentence-BERT' Embeddings

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tok >= 0.2.3
BuildRequires:    R-CRAN-onnxr >= 0.1.2
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-tok >= 0.2.3
Requires:         R-CRAN-onnxr >= 0.1.2
Requires:         R-CRAN-digest 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Builds semantic topic models from 'Sentence-BERT' embeddings (Reimers and
Gurevych, 2019) <doi:10.18653/v1/D19-1410>. Sentence embeddings are
computed in several modes with models run on the Open Neural Network
Exchange ('ONNX') Runtime, including multilingual and long-context
encoders and a fast static model. Topics are labeled with class-based term
weighting that can be retuned without refitting. Candidate topic counts
and document granularities (whole documents, sentences, clauses, or
phrases) can be compared side by side, and fitted models assign topics to
new documents, give soft memberships and per-document topic mixtures. The
package offers coherence and diversity metrics and visualizations.

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
