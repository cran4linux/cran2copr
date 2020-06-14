%global packname  R.oo
%global packver   1.23.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.23.0
Release:          2%{?dist}
Summary:          R Object-Oriented Programming with or without References

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R.methodsS3 >= 1.7.1
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-R.methodsS3 >= 1.7.1
Requires:         R-methods 
Requires:         R-utils 

%description
Methods and classes for object-oriented programming in R with or without
references.  Large effort has been made on making definition of methods as
simple as possible with a minimum of maintenance for package developers.
The package has been developed since 2001 and is now considered very
stable.  This is a cross-platform package implemented in pure R that
defines standard S3 classes without any tricks.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/misc
%{rlibdir}/%{packname}/INDEX
