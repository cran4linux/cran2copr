%global __brp_check_rpaths %{nil}
%global packname  Harvest.Tree
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Harvest the Classification Tree

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-rpart 
BuildRequires:    R-stats 
Requires:         R-rpart 
Requires:         R-stats 

%description
Aimed at applying the Harvest classification tree algorithm, modified
algorithm of classic classification tree.The harvested tree has advantage
of deleting redundant rules in trees, leading to a simplify and more
efficient tree model.It was firstly used in drug discovery field, but it
also performs well in other kinds of data, especially when the region of a
class is disconnected. This package also improves the basic harvest
classification tree algorithm by extending the field of data of algorithm
to both continuous and categorical variables. To learn more about the
harvest classification tree algorithm, you can go to
http://www.stat.ubc.ca/Research/TechReports/techreports/220.pdf for more
information.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
