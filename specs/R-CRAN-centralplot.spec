%global packname  centralplot
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Show the Strength of Relationships Between Centre and PeripheralItems

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-ggplot2 

%description
The degree of correlation between centre and peripheral items are shown by
the length of the line between them. You can self-define the length by
inputing the "distance" parameter. For example, you can input (1 -
Pearson's correlation coefficient) as "distance" so that the stronger the
correlation between centre and peripheral item, the nearer they will be in
this plot. Also, If you do a hypothesis test and the null hypothesis is
centre and peripheral items are the same, you can input -log(P) as
distance. To sum up, the stronger the correlation between centre and
peripheral is, the smaller the "distance" parameter should be. Due to its
high degree of freedom, it can be applied to many different circumstance.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
