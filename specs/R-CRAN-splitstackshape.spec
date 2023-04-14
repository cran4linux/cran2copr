%global __brp_check_rpaths %{nil}
%global packname  splitstackshape
%global packver   1.4.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.8
Release:          3%{?dist}%{?buildtag}
Summary:          Stack and Reshape Datasets After Splitting Concatenated Values

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.4
Requires:         R-CRAN-data.table >= 1.9.4

%description
Online data collection tools like Google Forms often export
multiple-response questions with data concatenated in cells. The
concat.split (cSplit) family of functions splits such data into separate
cells. The package also includes functions to stack groups of columns and
to reshape wide data, even when the data are "unbalanced"---something
which reshape (from base R) does not handle, and which melt and dcast from
reshape2 do not easily handle.

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
