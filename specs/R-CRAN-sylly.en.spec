%global __brp_check_rpaths %{nil}
%global packname  sylly.en
%global packver   0.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Language Support for 'sylly' Package: English

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-sylly 
Requires:         R-CRAN-sylly 

%description
Adds support for the English language to the 'sylly' package. Due to some
restrictions on CRAN, the full package sources are only available from the
project homepage. To ask for help, report bugs, suggest feature
improvements, or discuss the global development of the package, please
consider subscribing to the koRpus-dev mailing list
(<http://korpusml.reaktanz.de>).

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
