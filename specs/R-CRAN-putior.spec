%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  putior
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          "Register In- and Outputs for Workflow Visualization"

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-tools 
Requires:         R-tools 

%description
Provides tools for extracting and processing structured annotations from
'R' and 'Python' source files to facilitate workflow visualization. The
package scans source files for special 'PUT' annotations that define
nodes, connections, and metadata within a data processing workflow. These
annotations can then be used to generate visual representations of data
flows and processing steps across polyglot software environments. Builds
on concepts from literate programming Knuth (1984)
<doi:10.1093/comjnl/27.2.97> and utilizes directed acyclic graph (DAG)
theory for workflow representation Foraita, Spallek, and Zeeb (2014)
<doi:10.1007/978-0-387-09834-0_65>. Diagram generation powered by
'Mermaid' Sveidqvist (2014) <https://mermaid.js.org/>.

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
