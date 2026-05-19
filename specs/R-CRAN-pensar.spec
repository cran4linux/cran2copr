%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pensar
%global packver   0.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          1%{?dist}%{?buildtag}
Summary:          LLM Wiki Engine

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-yaml 

%description
Personal wiki engine with a large language model (LLM) as research
assistant. Supports guided sessions through a 'Claude Code'
<https://github.com/anthropics/claude-code> skill bundle and autonomous
research runs from R via autoresearch(). Results land in a structured
vault of markdown pages with 'YAML' frontmatter and wikilinks, ready for
hand-editing in your favourite editor alongside the LLM. Vaults are seeded
with 'CLAUDE.md' and 'AGENTS.md' so 'Claude Code', 'Codex'
<https://github.com/openai/codex>, and other agents share the same
operating instructions. Can adopt an existing 'Obsidian'
<https://obsidian.md/> vault in place via init_vault(adopt = TRUE).

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
