%global __brp_check_rpaths %{nil}
%global packname  TableToLongForm
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          3%{?dist}%{?buildtag}
Summary:          Automatically Convert Hierarchical for-Human Tables toMachine-Readable LongForm Dataframes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
A wrapper to a set of algorithms designed to recognise positional cues
present in hierarchical for-human Tables (which would normally be
interpreted visually by the human brain) to decompose, then reconstruct
the data into machine-readable LongForm Dataframes.

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
