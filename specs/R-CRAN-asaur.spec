%global __brp_check_rpaths %{nil}
%global packname  asaur
%global packver   0.50
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.50
Release:          3%{?dist}%{?buildtag}
Summary:          Data Sets for "Applied Survival Analysis Using R""

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Data sets are referred to in the text "Applied Survival Analysis Using R"
by Dirk F. Moore, Springer, 2016, ISBN: 978-3-319-31243-9,
<DOI:10.1007/978-3-319-31245-3>.

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
