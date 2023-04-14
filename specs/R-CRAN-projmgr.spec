%global __brp_check_rpaths %{nil}
%global packname  projmgr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Task Tracking and Project Management with GitHub

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-gh 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-gh 
Requires:         R-CRAN-magrittr 

%description
Provides programmatic access to 'GitHub' API with a focus on project
management.  Key functionality includes setting up issues and milestones
from R objects or 'YAML' configurations, querying outstanding or completed
tasks, and generating progress updates in tables, charts, and RMarkdown
reports. Useful for those using 'GitHub' in personal, professional, or
academic settings with an emphasis on streamlining the workflow of data
analysis projects.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
