%global packname  bsub
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Submitter and Monitor of the 'LSF Cluster'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-GetoptLong >= 0.1.8
BuildRequires:    R-CRAN-GlobalOptions >= 0.1.1
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-clisymbols 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-GetoptLong >= 0.1.8
Requires:         R-CRAN-GlobalOptions >= 0.1.1
Requires:         R-CRAN-digest 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-clisymbols 
Requires:         R-CRAN-crayon 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
It submits R code/R scripts/shell commands to 'LSF cluster'
(<https://en.wikipedia.org/wiki/Platform_LSF>, the 'bsub' system) without
leaving R. There is also an interactive 'shiny' app for monitoring the job
status.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
