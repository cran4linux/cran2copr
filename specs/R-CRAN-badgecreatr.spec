%global packname  badgecreatr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Create Badges for 'Travis', 'Repostatus' 'Codecov.io' Etc inGithub Readme

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4
Requires:         R-core >= 3.2.4
BuildArch:        noarch
BuildRequires:    R-CRAN-git2r 
Requires:         R-CRAN-git2r 

%description
Tired of copy and pasting almost identical markdown for badges in every
new R-package that you create, on Github or other code-sharing sites? This
package allows you to easily paste badges. If you want to, it will also
search your DESCRIPTION file and extract the package name, license,
R-version, and current projectversion and transform that into badges. It
will also search for a ".travis.yml" file and create a "Travis"" badge, if
you use "Codecov.io" to check your code coverage after a "Travis" build
this package will also build a "Codecov.io"-badge. All the badges can be
placed individually or can be placed below the top "YAML"" content of your
"RMarkdown file" (Readme.Rmd) or "README.md" file. Currently creates
badges for Projectstatus ("Repostatus.org"), license Travis Build Status,
Codecov, Minimal R version, CRAN status, CRAN downloads, Github stars and
forks, Package rank, rdocumentation, current version of your package and
last change of "README.Rmd".

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/README.Rmd
%{rlibdir}/%{packname}/INDEX
