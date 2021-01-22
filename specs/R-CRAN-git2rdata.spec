%global packname  git2rdata
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Store and Retrieve Data.frames in a Git Repository

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-git2r >= 0.23.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-git2r >= 0.23.0
Requires:         R-CRAN-assertthat 
Requires:         R-methods 
Requires:         R-CRAN-yaml 

%description
The git2rdata package is an R package for writing and reading dataframes
as plain text files.  A metadata file stores important information.  1)
Storing metadata allows to maintain the classes of variables.  By default,
git2rdata optimizes the data for file storage. The optimization is most
effective on data containing factors.  The optimization makes the data
less human readable.  The user can turn this off when they prefer a human
readable format over smaller files. Details on the implementation are
available in vignette("plain_text", package = "git2rdata").  2) Storing
metadata also allows smaller row based diffs between two consecutive
commits.  This is a useful feature when storing data as plain text files
under version control.  Details on this part of the implementation are
available in vignette("version_control", package = "git2rdata").  Although
we envisioned git2rdata with a git workflow in mind, you can use it in
combination with other version control systems like subversion or
mercurial.  3) git2rdata is a useful tool in a reproducible and traceable
workflow.  vignette("workflow", package = "git2rdata") gives a toy
example.  4) vignette("efficiency", package = "git2rdata") provides some
insight into the efficiency of file storage, git repository size and speed
for writing and reading.  Please cite using <doi:10.5281/zenodo.1485309>.

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
