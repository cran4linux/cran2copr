%global __brp_check_rpaths %{nil}
%global packname  josaplay
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Add Josa Based on Previous Letter in Korean

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-utf8 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-utf8 
Requires:         R-CRAN-magrittr 

%description
Josa in Korean is often determined by judging the previous word. When
writing reports using Rmd, a function that prints the appropriate
investigation for each case is helpful. The 'josaplay' package then
evaluates the previous word to determine which josa is appropriate.

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
